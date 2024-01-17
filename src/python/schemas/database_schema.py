from sqlalchemy import Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# Declarative base class

class Base(DeclarativeBase):
    pass

# Location Table
## Columns: PK_ID, Country, City, Street name and number, ZIP-Code, GPS Latitude, GPS Longitude (Primary key [GPS LAT+GPS LONG])

class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str]
    city: Mapped[str]
    street_name_num: Mapped[str]
    zip_code: Mapped[str] #To-do: for validation, split by '-', check if isinstance is int
    gps_lat = Mapped[float] # In the future, validate the convencional GPS coordinates (rad, min sec...)
    gps_lon = Mapped[float] # Same as gps_lat
    # TO DO: Set GPS LAT LONG into a Primary key constraint

# Questions Table
## PK_ID, Question, Correct_Answer, Answer_2, Answer_3, Answer_4, Fun_facts, Location.PK_ID

class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str]
    correct_answer: Mapped[str]
    answer_2: Mapped[str]
    answer_3: Mapped[str]
    answer_4: Mapped[str]
    fun_facts: Mapped[str]
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
