import { useId } from "react";
import { Select, SelectOption } from "@nous-research/ui/ui/components/select";
import { Switch } from "@nous-research/ui/ui/components/switch";
import { Input } from "@nous-research/ui/ui/components/input";
import { Label } from "@nous-research/ui/ui/components/label";

function FieldHint({ schema, schemaKey }: { schema: Record<string, unknown>; schemaKey: string }) {
  const keyPath = schemaKey.includes(".") ? schemaKey : "";
  const description = schema.description ? String(schema.description) : "";

  if (!keyPath && !description) return null;

  return (
    <div className="flex flex-col gap-0.5">
      {keyPath && <span className="text-xs font-mono text-text-tertiary">{keyPath}</span>}
      {description && <span className="text-xs text-text-secondary">{description}</span>}
    </div>
  );
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function formatScalar(value: unknown): string {
  if (value === undefined || value === null) return "";
  if (typeof value === "string") return value;
  if (typeof value === "number" || typeof value === "boolean") return String(value);
  return JSON.stringify(value);
}

function NestedValueEditor({
  fieldKey,
  value,
  onChange,
  id,
}: {
  fieldKey: string;
  value: unknown;
  onChange: (v: unknown) => void;
  id?: string;
}) {
  const innerId = useId();
  if (isRecord(value)) {
    return (
      <div className="grid gap-2 border border-border p-2">
        {Object.entries(value).map(([subKey, subVal]) => {
          const subId = `${innerId}-${subKey}`;
          return (
            <div key={subKey} className="grid gap-1">
              <Label htmlFor={subId} className="text-xs text-muted-foreground">{subKey}</Label>
              <NestedValueEditor
                fieldKey={`${fieldKey}.${subKey}`}
                value={subVal}
                onChange={(next) => onChange({ ...value, [subKey]: next })}
                id={subId}
              />
            </div>
          );
        })}
      </div>
    );
  }

  if (Array.isArray(value)) {
    return (
      <div className="grid gap-2">
        {value.map((item, index) => {
          const itemKey = `${innerId}-${index}`;
          return (
            <div key={`${fieldKey}.${index}`} className="grid gap-1">
              <Label htmlFor={itemKey} className="text-xs text-muted-foreground">Item {index + 1}</Label>
              <NestedValueEditor
                fieldKey={`${fieldKey}.${index}`}
                value={item}
                onChange={(next) =>
                  onChange(value.map((existing, i) => (i === index ? next : existing)))
                }
                id={itemKey}
              />
            </div>
          );
        })}
      </div>
    );
  }

  return (
    <Input
      id={id}
      value={formatScalar(value)}
      onChange={(e) => onChange(e.target.value)}
      className="text-xs"
    />
  );
}

export function AutoField({
  schemaKey,
  schema,
  value,
  onChange,
}: AutoFieldProps) {
  const id = useId();
  const rawLabel = schemaKey.split(".").pop() ?? schemaKey;
  const label = rawLabel.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

  if (isRecord(value) || (Array.isArray(value) && value.some((item) => isRecord(item)))) {
    return (
      <div className="grid gap-3 border border-border p-3">
        <Label className="text-xs font-medium">{label}</Label>
        <FieldHint schema={schema} schemaKey={schemaKey} />
        <NestedValueEditor fieldKey={schemaKey} value={value} onChange={onChange} />
      </div>
    );
  }

  if (schema.type === "boolean") {
    return (
      <div className="flex items-center justify-between gap-4">
        <div className="flex flex-col gap-0.5">
          <Label htmlFor={id} className="text-sm">{label}</Label>
          <FieldHint schema={schema} schemaKey={schemaKey} />
        </div>
        <Switch id={id} checked={!!value} onCheckedChange={onChange} />
      </div>
    );
  }

  if (schema.type === "select") {
    const options = (schema.options as string[]) ?? [];
    return (
      <div className="grid gap-1.5">
        <Label htmlFor={id} className="text-sm">{label}</Label>
        <FieldHint schema={schema} schemaKey={schemaKey} />
        <Select id={id} value={String(value ?? "")} onValueChange={(v) => onChange(v)}>
          {options.map((opt) => (
            <SelectOption key={opt} value={opt}>
              {opt || "(none)"}
            </SelectOption>
          ))}
        </Select>
      </div>
    );
  }

  if (schema.type === "number") {
    return (
      <div className="grid gap-1.5">
        <Label htmlFor={id} className="text-sm">{label}</Label>
        <FieldHint schema={schema} schemaKey={schemaKey} />
        <Input
          id={id}
          type="number"
          value={value === undefined || value === null ? "" : String(value)}
          onChange={(e) => {
            const raw = e.target.value;
            if (raw === "") {
              onChange(0);
              return;
            }
            const n = Number(raw);
            if (!Number.isNaN(n)) {
              onChange(n);
            }
          }}
        />
      </div>
    );
  }

  if (schema.type === "text") {
    return (
      <div className="grid gap-1.5">
        <Label htmlFor={id} className="text-sm">{label}</Label>
        <FieldHint schema={schema} schemaKey={schemaKey} />
        <textarea
          id={id}
          className="flex min-h-[80px] w-full border border-input bg-transparent px-3 py-2 text-sm shadow-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
          value={String(value ?? "")}
          onChange={(e) => onChange(e.target.value)}
        />
      </div>
    );
  }

  if (schema.type === "list") {
    return (
      <div className="grid gap-1.5">
        <Label htmlFor={id} className="text-sm">{label}</Label>
        <FieldHint schema={schema} schemaKey={schemaKey} />
        <Input
          id={id}
          value={Array.isArray(value) ? value.join(", ") : String(value ?? "")}
          onChange={(e) =>
            onChange(
              e.target.value
                .split(",")
                .map((s) => s.trim())
                .filter(Boolean),
            )
          }
          placeholder="comma-separated values"
        />
      </div>
    );
  }

  return (
    <div className="grid gap-1.5">
      <Label htmlFor={id} className="text-sm">{label}</Label>
      <FieldHint schema={schema} schemaKey={schemaKey} />
      <Input id={id} value={String(value ?? "")} onChange={(e) => onChange(e.target.value)} />
    </div>
  );
}

interface AutoFieldProps {
  schemaKey: string;
  schema: Record<string, unknown>;
  value: unknown;
  onChange: (v: unknown) => void;
}
