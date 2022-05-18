# Create a test client using the Flask application configured for testing
import pytest
from faker import Faker

from app.models import db, User

from app.routes import app

fake= Faker()

@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
       with app.app_context():
            yield client

@pytest.fixture
def init_database():
    #   create the database and database table
    db.create_all()
    # create a list of test users
    test_users =[{
        "name":fake.name(),
        "username":fake.username(),
        "company":fake.company(),
        "jobtitle":fake.jobtitle(),
        "email":fake.email(),
        "password":fake.password()
    }]
    #  convert a list of dictionaries to a list of user objects
    def create_post_model(user):
        return User(**user)
    # Create a list of User objects
    mapped_users = map(create_post_model, test_users)
    t_users = list(mapped_users)

     # Add the users to the database - add_all() is used to add multiple records
    db.session.add_all(t_users)

     # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!
    db.session.remove()  # looks like db.session.close() would work as well
    db.drop_all()