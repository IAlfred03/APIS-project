from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3000",  # React dev server URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/violations")
async def get_violations():
    # Returning a list of violations as JSON data
    return [
        {"id": "node/2987728504", "latitude": 38.9294, "longitude": -77.02307, "location": "Some location", "distance_to_building": 50},
        {"id": "node/2989827824", "latitude": 38.97898, "longitude": -77.02623, "location": "Another location", "distance_to_building": 40},
        {"id": "node/11379610369", "latitude": 38.89647, "longitude": -77.00788, "location": "Third location", "distance_to_building": 30}
    ]
    
@app.get("/")
def read_root():
    return {"message": "Welcome to the NESC API"}
