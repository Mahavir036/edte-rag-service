import pytest

from src.services.chunking import chunk_text


def test_chunk_text_splits_correctly() -> None:
    text = "A" * 1200

    chunks = chunk_text(text)

    assert len(chunks) == 3
    assert [len(chunk) for chunk in chunks] == [500, 500, 300]


def test_chunk_text_has_overlap() -> None:
    text = "A" * 1200
    chunks = chunk_text(text)

    assert chunks[0][-50:] == chunks[1][:50]


def test_chunk_text_empty_input() -> None:
    assert chunk_text("") == []


def test_chunk_text_strips_whitespace() -> None:
    assert chunk_text("           ") == []


def test_chunk_text_rejects_invalid_chunk_size() -> None:
    with pytest.raises(ValueError):
        chunk_text("Hello", chunk_size=0)


def test_chunk_text_rejects_invalid_overlap() -> None:
    with pytest.raises(ValueError):
        chunk_text("Hello", chunk_size=100, overlap=100)


def test_chunk_text_rejects_non_string_input() -> None:
    with pytest.raises(TypeError):
        chunk_text(123)  # typ : ignore[arg-type]


def test_chunk_text_rejects_non_integar_chunk_size() -> None:
    with pytest.raises(TypeError):
        chunk_text("Hello", chunk_size=100.5)  # type : ignore[arg-type]


def test_chunk_text_rejects_non_integer_overlap() -> None:
    with pytest.raises(TypeError):
        chunk_text("Hello", overlap=2.5)  # type : ignore[arg - type]
