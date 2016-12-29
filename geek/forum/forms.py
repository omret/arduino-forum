from django import forms

class NewTopicForm(forms.Form):
    ##-------the form of title------------
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={"id": "titleform",
                                       "class": "form-control"}
                            ))

    content = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={"id": "omrettinymce"}
                              ))
