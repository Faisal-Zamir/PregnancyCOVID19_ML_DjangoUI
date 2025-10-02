from django import forms

class PregnancyForm(forms.Form):
    Maternal_Age = forms.IntegerField(
        min_value=18, 
        max_value=50,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Age in years'
        })
    )
    
    Income_Cleaned = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Annual income amount'
        })
    )

    Maternal_Education_encoded = forms.ChoiceField(
        choices=[
            (0, "Less than high school diploma"),
            (1, "High school diploma"),
            (2, "College/trade school"),
            (3, "Undergraduate degree"),
            (4, "Masters degree"),
            (5, "Doctoral Degree"),
            (-1, "Unknown")
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    Edinburgh_Postnatal_Depression_Scale = forms.IntegerField(
        min_value=0, 
        max_value=30,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Score (0-30)'
        })
    )
    
    PROMIS_Anxiety = forms.IntegerField(
        min_value=0, 
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Anxiety score'
        })
    )
    
    Gestational_Age_At_Birth = forms.FloatField(
        min_value=20, 
        max_value=42,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Weeks of gestation',
            'step': '0.1'
        })
    )
    
    Birth_Length = forms.FloatField(
        min_value=30, 
        max_value=60,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Length in cm',
            'step': '0.1'
        })
    )
    
    Birth_Weight = forms.IntegerField(
        min_value=500, 
        max_value=5000,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Weight in grams'
        })
    )

    DeliveryMode = forms.ChoiceField(
        choices=[
            ("cesarean", "Cesarean Section"),
            ("vaginal", "Vaginal Delivery"),
            ("unknown", "Unknown")
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    Language_mapped = forms.ChoiceField(
        choices=[
            (1, "English"),
            (0, "French"),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    Threaten_Life = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    Threaten_Baby_Danger = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    Threaten_Baby_Harm = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    Year = forms.ChoiceField(
        choices=[(y, y) for y in range(2000, 2031)],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    Month = forms.ChoiceField(
        choices=[(m, m) for m in range(1, 13)],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    NICU_missing_flag = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )