from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class DeckForm(FlaskForm):
    name = StringField("Deck Name")
    description = StringField("Description")
    category    = StringField("Category")
    submit = SubmitField("Create Deck")

    
class CardForm(FlaskForm):
    deck = SelectField('Deck', coerce=int)
    question = TextAreaField("Question")
    answer = TextAreaField("Answer")
    submit = SubmitField("Save Card")
    
class EditCardForm(FlaskForm):
    question = TextAreaField('Question')
    answer   = TextAreaField('Answer')
    submit   = SubmitField('Save Changes')