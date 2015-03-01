from rest_framework import serializers

from questions.models import Choice


class ChoiceRelatedField(serializers.SlugRelatedField):
    """
    A read-write field the represents the target of the relationship by a unique 'slug' attribute.
    """

    default_error_messages = {
        'does_not_exist': "No choice with '{value}' id.",
        'invalid': 'Invalid value.',
    }

    def to_internal_value(self, uuid):
        try:
            return self.context['view'].get_question().choices.get(**{self.slug_field: uuid})
        except Choice.DoesNotExist:
            self.fail('does_not_exist', value=uuid)
        except (TypeError, ValueError):
            self.fail('invalid')
