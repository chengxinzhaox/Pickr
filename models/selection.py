from .db_instance import db


class Selection(db.Model):
    __tablename__ = 'selections'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship('Student', foreign_keys=[student_id])
    submit_time = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    first_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    second_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    third_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    final_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    first_topic = db.relationship('Topic', foreign_keys=[first_topic_id])
    second_topic = db.relationship('Topic', foreign_keys=[second_topic_id])
    third_topic = db.relationship('Topic', foreign_keys=[third_topic_id])
    final_topic = db.relationship('Topic', foreign_keys=[final_topic_id])

    def __init__(self, student_id):
        self.student_id = student_id
        self.status = 0

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self, student_id, submit_time, status, first_topic_id, second_topic_id, third_topic_id, final_topic_id):
        self.student_id = student_id
        self.submit_time = submit_time
        self.status = status
        self.first_topic_id = first_topic_id
        self.second_topic_id = second_topic_id
        self.third_topic_id = third_topic_id
        self.final_topic_id = final_topic_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def first_topic_name(self):
        return self.first_topic.name

    @property
    def first_topic_supervisor_name(self):
        return self.first_topic.supervisor.first_name + ' ' + self.first_topic.supervisor.last_name

    @property
    def final_topic_supervisor_name(self):
        return self.final_topic.supervisor.first_name + ' ' + self.final_topic.supervisor.last_name

    @property
    def final_topic_supervisor_email(self):
        return self.final_topic.supervisor.email

    @property
    def english_name(self):
        return self.student.english_name

    @property
    def chinese_name(self):
        return self.student.chinese_name

    @property
    def class_number(self):
        return self.student.class_number

    # if is custom selection, return true
    @property
    def if_custom(self):
        if not self.first_topic:
            return False
        return self.first_topic.is_custom

    @property
    def custom_supervisor_id(self):
        return self.first_topic.supervisor_id

    @property
    def custom_supervisor_name(self):
        return self.first_topic.supervisor.first_name + ' ' + self.first_topic.supervisor.last_name

    @property
    def custom_type_id(self):
        return self.first_topic.type_id

    @property
    def custom_type_name(self):
        return self.first_topic.type.name

    @property
    def final_type_name(self):
        return self.final_topic.type.name

    @property
    def custom_description(self):
        return self.first_topic.description

    @property
    def second_topic_name(self):
        return self.second_topic.name

    @property
    def third_topic_name(self):
        return self.third_topic.name

    @property
    def final_topic_name(self):
        return self.final_topic.name

    @classmethod
    def get_by_student_id(cls, student_id):
        return cls.query.filter_by(student_id=student_id).first()

    @classmethod
    def get_all_custom_selections(cls):
        return cls.query.filter(cls.status.in_([2, 3])).all()

    @classmethod
    def get_by_id(cls, selection_id):
        return cls.query.filter_by(id=selection_id).first()

    # get student name
    @classmethod
    def get_student_name(cls, student_id):
        return cls.query.filter_by(student_id=student_id).first().student.english_name

    # get number of status equal to 3 or 4 (success)
    @classmethod
    def get_num_of_status_3or4(cls):
        return cls.query.filter(cls.status.in_([3, 4])).count()

    def update_status(self, status):
        self.status = status

    def update_first_topic_supervisor_id(self, supervisor_id):
        self.first_topic.supervisor_id = supervisor_id
        db.session.commit()

    def update_first_topic_type_id(self, type_id):
        self.first_topic.type_id = type_id
        db.session.commit()

    def update_first_topic_description(self, description):
        self.first_topic.description = description
        db.session.commit()

    def update_first_topic_name(self, name):
        self.first_topic.name = name
        db.session.commit()

    def __repr__(self):
        return f'<Selection {self.id}>'
