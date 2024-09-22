from django import forms
from .models import Paciente, Profissional, Transacao, Agendamento


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            "nome",
            "idade",
            "sexo",
            "altura",
            "peso",
        ]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome do paciente"}
            ),
            "idade": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Idade do paciente"}
            ),
            "sexo": forms.Select(
                attrs={"class": "form-control", "placeholder": "Sexo do paciente"},
            ),
            "altura": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Altura do paciente"}
            ),
            "peso": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Peso do paciente"}
            ),
        }

    def clean_nome(self):
        nome = self.cleaned_data["nome"]
        if len(nome) < 3:
            raise forms.ValidationError("Nome deve ter mais de 3 caracteres")
        return nome

    def clean_idade(self):
        idade = self.cleaned_data["idade"]
        if idade < 0:
            raise forms.ValidationError("Idade não pode ser negativa")
        elif idade > 120:
            raise forms.ValidationError("Idade não pode ser maior que 120 anos")
        return idade

    def clean_altura(self):
        altura = self.cleaned_data["altura"]
        if altura < 0:
            raise forms.ValidationError("Altura não pode ser negativa")
        elif altura > 3:
            raise forms.ValidationError("Altura não pode ser maior que 3 metros")
        return altura

    def clean_peso(self):
        peso = self.cleaned_data["peso"]
        if peso < 0:
            raise forms.ValidationError("Peso não pode ser negativo")
        elif peso > 300:
            raise forms.ValidationError("Peso não pode ser maior que 300 kg")
        return peso


class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = [
            "nome",
            "especialidade",
            "registro_profissional",
        ]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome do profissional"}
            ),
            "especialidade": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Especialidade do profissional",
                }
            ),
            "registro_profissional": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Registro profissional do profissional",
                }
            ),
        }

    def clean_nome(self):
        nome = self.cleaned_data["nome"]
        if len(nome) < 3:
            raise forms.ValidationError("Nome deve ter mais de 3 caracteres")
        return nome

    def clean_especialidade(self):
        especialidade = self.cleaned_data["especialidade"]
        if len(especialidade) < 3:
            raise forms.ValidationError("Especialidade deve ter mais de 3 caracteres")
        return especialidade

    def clean_registro_profissional(self):
        registro_profissional = self.cleaned_data["registro_profissional"]
        if len(registro_profissional) < 3:
            raise forms.ValidationError(
                "Registro profissional deve ter mais de 3 caracteres"
            )
        return registro_profissional


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = [
            "paciente",
            "profissional",
            "valor",
            "tipo",
            "descricao",
        ]
        widgets = {
            "paciente": forms.Select(
                attrs={"class": "form-control", "placeholder": "Paciente"}
            ),
            "profissional": forms.Select(
                attrs={"class": "form-control", "placeholder": "Profissional"}
            ),
            "valor": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Valor da transação"}
            ),
            "tipo": forms.Select(
                attrs={"class": "form-control", "placeholder": "Tipo da transação"},
            ),
            "descricao": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descrição da transação"}
            ),
        }


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = [
            "paciente",
            "profissional",
            "data_horario",
            "confirmado",
        ]
        widgets = {
            "paciente": forms.Select(
                attrs={"class": "form-control", "placeholder": "Paciente"}
            ),
            "profissional": forms.Select(
                attrs={"class": "form-control", "placeholder": "Profissional"}
            ),
            "data_horario": forms.DateTimeInput(
                format="%Y-%m-%d %H:%M:%S",
                attrs={
                    "type": "datetime-local",
                    "class": "form-control datetimepicker-input",
                },
            ),
            "confirmado": forms.CheckboxInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Agendamento confirmado",
                },
            ),
        }
