from nest.core.database.orm_provider import AsyncOrmProvider
import os
from dotenv import load_dotenv
    
load_dotenv()
    
config = AsyncOrmProvider(
    db_type="mysql",
    config_params=dict(
        host="db",
        db_name="atlasdb",
        user="root",
        password="root",
        port=int("3306"),        
    )
)
