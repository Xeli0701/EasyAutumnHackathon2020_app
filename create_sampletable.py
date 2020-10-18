from models import *
import db
import os

#password設定などがあるので気をつけること

if __name__ == "__main__":
    Base.metadata.create_all(db.engine)

    # SampleUserを追加
    sample = User(username='user', password='123456', mail='hoge@example.com')
    db.session.add(sample)
    db.session.commit()
    db.session.close()