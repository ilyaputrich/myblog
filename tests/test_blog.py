import pytest
import httpx


SERVER = "http://localhost:8000"

def test_blog() -> None:
    url: str = f"{SERVER}/"
    resp = httpx.get(url)
    assert resp.status_code == 200

def test_blog_id() -> None:
    url: str = f"{SERVER}/9"
    resp = httpx.get(url)
    assert resp.status_code == 200

def test_blog_search() -> None:
    url: str = f"{SERVER}/search?search=машин"
    resp = httpx.get(url)
    assert resp.status_code == 200
    assert "машин" in resp.text
