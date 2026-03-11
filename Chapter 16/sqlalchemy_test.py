# import sqlalchemy as sa

# # 1. 엔진 생성 (변수명을 engine으로 변경하는 것이 일반적인 관례입니다)
# engine = sa.create_engine('sqlite://')

# # 2. Connection 객체 생성 (begin()을 사용하면 작업 종료 시 자동 커밋됩니다)
# with engine.begin() as conn:

#     # 3. 테이블 생성 (SQL 문자열을 sa.text로 감쌈)
#     conn.execute(sa.text('''
#         CREATE TABLE zoo
#         (critter VARCHAR(20) PRIMARY KEY,
#         count INT,
#         damages FLOAT)
#     '''))

#     # 4. 데이터 삽입 (명명된 파라미터 :critter, :count, :damages 사용)
#     ins = sa.text('INSERT INTO zoo (critter, count, damages) VALUES (:critter, :count, :damages)')

#     # 여러 개의 데이터를 딕셔너리 리스트로 묶어서 한 번에 전달
#     data = [
#         {"critter": 'duck', "count": 10, "damages": 0.0},
#         {"critter": 'bear', "count": 2, "damages": 1000.0},
#         {"critter": 'weasel', "count": 1, "damages": 2000.0}
#     ]
#     conn.execute(ins, data)

#     # 5. 데이터 조회
#     rows = conn.execute(sa.text('SELECT * FROM zoo'))

#     # 결과를 반복문으로 출력하거나 fetchall()로 가져옵니다
#     for row in rows:
#         print(row)


# import sqlalchemy as sa

# engine = sa.create_engine('sqlite://')

# # 메타데이터 생성 및 테이블 정의
# meta = sa.MetaData()
# zoo = sa.Table('zoo', meta,
#             sa.Column('critter', sa.String, primary_key=True),
#             sa.Column('count', sa.Integer),
#             sa.Column('damages', sa.Float)
#             )

# # 테이블 생성 (engine을 통해 DB에 반영)
# meta.create_all(engine)

# with engine.begin() as conn:
#     # 1. Insert 쿼리문 객체 생성
#     stmt = zoo.insert()
    
#     # 2. execute()에 쿼리문과 데이터를 분리해서 전달 (딕셔너리 리스트 사용)
#     # 한 줄씩 넣는 것보다 이렇게 리스트로 묶어서 한 번에 넣는 것이 훨씬 효율적입니다.
#     data = [
#         {"critter": 'bear', "count": 2, "damages": 1000.0},
#         {"critter": 'weasel', "count": 1, "damages": 2000.0},
#         {"critter": 'duck', "count": 10, "damages": 0.0}
#     ]
#     conn.execute(stmt, data)

#     # 3. 데이터 조회
#     result = conn.execute(zoo.select())
#     rows = result.fetchall()
    
#     print(rows)


# import sqlalchemy as sa
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# # 1. 엔진 생성
# engine = sa.create_engine('sqlite:///zoo.db')

# # 2. Base 클래스 정의 (2.0에서는 함수 대신 클래스 상속 방식을 사용합니다)
# class Base(DeclarativeBase):
#     pass

# # 3. 모델 클래스 정의 (Mapped와 mapped_column을 사용하여 타입 힌트를 명시합니다)
# class Zoo(Base):
#     __tablename__ = 'zoo'
    
#     # 파이썬의 타입(str, int, float)을 명시해주면 IDE에서 자동완성 지원이 훨씬 좋아집니다.
#     critter: Mapped[str] = mapped_column(sa.String, primary_key=True)
#     count: Mapped[int] = mapped_column(sa.Integer)
#     damages: Mapped[float] = mapped_column(sa.Float)
    
#     # SQLAlchemy 2.0에서는 __init__ 메서드를 명시적으로 작성하지 않아도
#     # 기본적으로 키워드 인자(kwargs)를 받는 __init__을 자동 생성해 줍니다.
    
#     def __repr__(self) -> str:
#         return f"<Zoo(critter={self.critter}, count={self.count}, damages={self.damages})>"

# # 4. 테이블 생성 (engine을 사용해 생성합니다)
# Base.metadata.create_all(engine)

# # 5. Session을 사용한 데이터 삽입
# # 2.0에서는 Core의 engine.begin() 대신 ORM 전용인 with Session(engine)을 사용합니다.
# with Session(engine) as session:
#     # 키워드 인자로 데이터를 생성합니다.
#     first = Zoo(critter='duck', count=10, damages=0.0)
#     second = Zoo(critter='bear', count=2, damages=1000.0)
#     third = Zoo(critter='weasel', count=1, damages=2000.0)
    
#     print(first)

#     # 세션에 데이터 추가
#     session.add(first)
#     session.add_all([second, third])
    
#     # DB에 반영
#     session.commit()