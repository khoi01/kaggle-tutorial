import pytest
import asyncio

@pytest.mark.asyncio
async def test_example():
    await asyncio.sleep(0.1)
    assert 1 + 1 == 2