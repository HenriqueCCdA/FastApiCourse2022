from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def get_compay_name():
    return {"company_name": "Example Company, LLC"}


@router.get("/employees")
async def number_of_employess():
    return 162