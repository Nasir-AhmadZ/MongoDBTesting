def individual_data(todo):
    return{
        "id":str(todo["_id"]),
        "title":str(todo["title"]),
        "description":str(todo["description"]),
        "status":str(todo["is_completed"])
        
    }