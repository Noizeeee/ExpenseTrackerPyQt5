from backend.supabase_client import supabase

def get_all_expenses():
    response = (
        supabase
        .table("expenses")
        .select("*")
        .execute()
    )

    return response.data