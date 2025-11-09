# backend/tyres_service/load_csv.py
import csv
from decimal import Decimal
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import TyreModel

Base.metadata.create_all(bind=engine)

CSV_FILE = "tyredatabase.csv"

def to_bool(value: str) -> bool:
    """Convert CSV TRUE/FALSE to Python bool safely"""
    return str(value).strip().lower() in ("true", "1", "yes")

def load_csv():
    db: Session = SessionLocal()
    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                # normalize column names
                tyre = TyreModel(
                    size=row["size"].strip(),
                    load_rate=int(row["load_rate"]),
                    speed_rate=row["speed_rate"].strip(),
                    brand=row["Brand"].strip(),
                    model=row["Model"].strip(),
                    season=row["Season"].strip().capitalize(),
                    supplier=row["Supplier"].strip(),
                    fuel_efficiency=row["Fuel_Efficiency"].strip().upper(),
                    noise_level=int(row["noise_level"]),
                    weather_efficiency=row["weather_efficiency"].strip().upper(),
                    ev_approved=to_bool(row["ev_approved"]),
                    cost=Decimal(str(row["cost"])),
                    quantity=int(row["quantity"]),
                    retail_cost=Decimal(str(row["cost"])) * Decimal("1.35"),
                )
                db.add(tyre)
                count += 1

            db.commit()
            print(f"Successfully inserted {count} tyres into the database.")

    except FileNotFoundError:
        print(f"Could not find CSV file: {CSV_FILE}")
    finally:
        db.close()

if __name__ == "__main__":
    load_csv()
