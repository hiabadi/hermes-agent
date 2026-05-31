"""Tests for the todo tool module."""

import json

from tools.todo_tool import TodoStore, todo_tool


class TestWriteAndRead:
    def test_write_replaces_list(self):
        store = TodoStore()
        items = [
            {"id": "1", "content": "First task", "status": "pending"},
            {"id": "2", "content": "Second task", "status": "in_progress"},
        ]
        result = store.write(items)
        assert len(result) == 2
        assert result[0]["id"] == "1"
        assert result[1]["status"] == "in_progress"

    def test_read_returns_copy(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "Task", "status": "pending"}])
        items = store.read()
        items[0]["content"] = "MUTATED"
        assert store.read()[0]["content"] == "Task"

    def test_write_deduplicates_duplicate_ids(self):
        store = TodoStore()
        result = store.write([
            {"id": "1", "content": "First version", "status": "pending"},
            {"id": "2", "content": "Other task", "status": "pending"},
            {"id": "1", "content": "Latest version", "status": "in_progress"},
        ])
        assert result == [
            {"id": "2", "content": "Other task", "status": "pending"},
            {"id": "1", "content": "Latest version", "status": "in_progress"},
        ]


class TestHasItems:
    def test_empty_store(self):
        store = TodoStore()
        assert store.has_items() is False

    def test_non_empty_store(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "x", "status": "pending"}])
        assert store.has_items() is True


class TestFormatForInjection:
    def test_empty_returns_none(self):
        store = TodoStore()
        assert store.format_for_injection() is None

    def test_non_empty_has_markers(self):
        store = TodoStore()
        store.write([
            {"id": "1", "content": "Do thing", "status": "completed"},
            {"id": "2", "content": "Next", "status": "pending"},
            {"id": "3", "content": "Working", "status": "in_progress"},
        ])
        text = store.format_for_injection()
        # Completed items are filtered out of injection
        assert "[x]" not in text
        assert "Do thing" not in text
        # Active items are included
        assert "[ ]" in text
        assert "[>]" in text
        assert "Next" in text
        assert "Working" in text
        assert "context compression" in text.lower()


class TestMergeMode:
    def test_update_existing_by_id(self):
        store = TodoStore()
        store.write([
            {"id": "1", "content": "Original", "status": "pending"},
        ])
        store.write(
            [{"id": "1", "status": "completed"}],
            merge=True,
        )
        items = store.read()
        assert len(items) == 1
        assert items[0]["status"] == "completed"
        assert items[0]["content"] == "Original"

    def test_merge_appends_new(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "First", "status": "pending"}])
        store.write(
            [{"id": "2", "content": "Second", "status": "pending"}],
            merge=True,
        )
        items = store.read()
        assert len(items) == 2


    def test_empty_id_skipped_during_merge(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "First", "status": "pending"}])
        store.write(
            [{"id": " ", "content": "No ID", "status": "pending"}],
            merge=True,
        )
        items = store.read()
        assert len(items) == 1
        assert items[0]["id"] == "1"

    def test_invalid_status_ignored_during_merge(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "Original", "status": "pending"}])
        store.write(
            [{"id": "1", "status": "invalid_status"}],
            merge=True,
        )
        items = store.read()
        assert len(items) == 1
        assert items[0]["status"] == "pending"

    def test_missing_fields_during_merge_ignored(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "Original", "status": "pending"}])
        store.write(
            [{"id": "1"}], # No content or status
            merge=True,
        )
        items = store.read()
        assert len(items) == 1
        assert items[0]["content"] == "Original"
        assert items[0]["status"] == "pending"

    def test_merge_appends_new_and_validates(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "First", "status": "pending"}])
        store.write(
            [{"id": "2", "status": "invalid"}], # New item without content, invalid status
            merge=True,
        )
        items = store.read()
        assert len(items) == 2
        assert items[1]["id"] == "2"
        assert items[1]["content"] == "(no description)"
        assert items[1]["status"] == "pending"


class TestValidation:
    def test_validate_missing_and_empty_fields(self):
        store = TodoStore()
        store.write([{}]) # Empty item
        items = store.read()
        assert len(items) == 1
        assert items[0]["id"] == "?"
        assert items[0]["content"] == "(no description)"
        assert items[0]["status"] == "pending"

    def test_validate_invalid_status_falls_back_to_pending(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "Task", "status": "done"}])
        items = store.read()
        assert items[0]["status"] == "pending"

    def test_validate_whitespace_fields(self):
        store = TodoStore()
        store.write([{"id": "   ", "content": " \n\t ", "status": "   "}])
        items = store.read()
        assert items[0]["id"] == "?"
        assert items[0]["content"] == "(no description)"
        assert items[0]["status"] == "pending"

    def test_validate_non_string_fields(self):
        store = TodoStore()
        store.write([{"id": 123, "content": ["not", "string"], "status": None}])
        items = store.read()
        assert items[0]["id"] == "123"
        assert items[0]["content"] == "['not', 'string']"
        assert items[0]["status"] == "pending"


class TestTodoToolFunction:
    def test_read_mode(self):
        store = TodoStore()
        store.write([{"id": "1", "content": "Task", "status": "pending"}])
        result = json.loads(todo_tool(store=store))
        assert result["summary"]["total"] == 1
        assert result["summary"]["pending"] == 1

    def test_write_mode(self):
        store = TodoStore()
        result = json.loads(todo_tool(
            todos=[{"id": "1", "content": "New", "status": "in_progress"}],
            store=store,
        ))
        assert result["summary"]["in_progress"] == 1

    def test_no_store_returns_error(self):
        result = json.loads(todo_tool())
        assert "error" in result
