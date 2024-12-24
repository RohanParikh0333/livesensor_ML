from fastapi import FastAPI
app = FastAPI()

@app.get("/Hello")
async def hello():
    return {"message":"Hello Python"}



indian_places = {
    'delhi': ['Red Fort', 'Qutub Minar', 'India Gate'],
    'mumbai': ['Gateway of India', 'Marine Drive', 'Elephanta Caves'],
    'jaipur': ['Hawa Mahal', 'Amber Fort', 'City Palace'],
    'varanasi': ['Kashi Vishwanath Temple', 'Ghats of Ganges', 'Sarnath'],
    'goa': ['Baga Beach', 'Calangute Beach', 'Dudhsagar Falls']
}

@app.get("/get_items/{name}")
async def hello(name):
    return indian_places.get(name)
