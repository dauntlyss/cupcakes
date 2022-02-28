from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="vanilla",
    size="medium",
    rating=10,
    image="https://images.unsplash.com/photo-1519869325930-281384150729?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHZhbmlsbGElMjBjdXBjYWtlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
)

c4 = Cupcake(
    flavor="carrot",
    size="small",
    rating=4,
    image="https://images.unsplash.com/photo-1487124504955-e42a39e11aaf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1426&q=80"
)

c5 = Cupcake(
    flavor="lemon",
    size="medium",
    rating=2,
    image="https://images.unsplash.com/photo-1608847567708-1e0b5a46eb13?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=686&q=80"
)

db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()