from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost/basesye")

meta = MetaData()

conn = engine.connect()