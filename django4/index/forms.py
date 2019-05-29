from django import forms

TOPIC_CHOICE = (('1','好评'),('2','中评'),('3','差评'))

class RemarkForm(forms.Form):
    subject = forms.CharField(label='标题')
    email = forms.EmailField(label='邮箱')
    message = forms.CharField(label='内容',widget=forms.Textarea)
    topic = forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
    isSaved = forms.BooleanField(label='是否保存')
