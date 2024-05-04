from fastapi import APIRouter, status, HTTPException
from schemas import Exerc02, Exerc03, Exerc04, Exerc05, Exerc06

exerc_router = APIRouter()


@exerc_router.get("/2")
async def exerc02():
    return Exerc02.get()


@exerc_router.get("/3")
async def exerc03():
    return Exerc03.get()


@exerc_router.get("/4")
async def exerc04():
    return Exerc04.get()


@exerc_router.get("/5")
async def exerc05():
    return Exerc05.get()


@exerc_router.get("/6")
async def exerc06():
    return Exerc06.get()
