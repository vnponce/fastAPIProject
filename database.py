from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost3306/fastapi")
meta = MetaData()

connect = engine.connect()
