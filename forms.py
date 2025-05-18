from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField,HiddenField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed
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

class csvForm(FlaskForm):
    deck = SelectField("Deck", coerce=int ,validators=[DataRequired()])
    csv = FileField("CSV File", validators=[DataRequired(), FileAllowed(["csv"], "only csv files")])
    submit = SubmitField("Import")
    
class StudyForm(FlaskForm):
    card_index = HiddenField(validators=[DataRequired()])
    previous   = SubmitField("Previous")
    next       = SubmitField("Next")
    studied    = SubmitField("Studied")