from nest.core.database.orm_provider import AsyncOrmProvider
import os
from dotenv import load_dotenv
    
load_dotenv()
    
config = AsyncOrmProvider(
    db_type="mysql",
    config_params=dict(
        host="127.0.0.1",
        db_name="dog",
        user="root",
        password="root",
        port=int("3306"),        
    )
)
