from django.contrib import admin
from .models import Countries, PeopleGroups, People, TypesLex, TypesMed, LessonBlocks, Lessons
from .models import Lexemes, Media, Ik, Replicas, LecFilling, Rules, RulesLexemes, TypesEx
from .models import Exercises, Progress, Tasks, Variants, Favorites
from .models import Newletters, Newwords, Newphrases, Matchsyllablessound, Collectwordsletters, Missingletter
from .models import Pronunciationwords, Recoverphrases, Selectwords, Wordpicturematch, Wordpictureselect, Writewords


# Register your models here.

# admin.site.register(Countries)


@admin.register(Countries)
class CountriesModel(admin.ModelAdmin):
    list_filter = ('id_country', 'country_name', 'flag_link')
    list_display = ('id_country', 'country_name', 'flag_link')


@admin.register(PeopleGroups)
class PeopleGroupsModel(admin.ModelAdmin):
    list_filter = ('group_user',)
    list_display = ('group_user',)


@admin.register(People)
class PeopleModel(admin.ModelAdmin):
    list_filter = ('login', 'surname', 'name', 'group_user', 'email', 'password', 'password_admin')
    list_display = ('login', 'surname', 'name', 'group_user', 'email', 'password', 'password_admin')


@admin.register(TypesLex)
class TypesLexModel(admin.ModelAdmin):
    list_filter = ('type_lex',)
    list_display = ('type_lex',)


@admin.register(TypesMed)
class TypesMedModel(admin.ModelAdmin):
    list_filter = ('type_med',)
    list_display = ('type_med',)


@admin.register(LessonBlocks)
class LessonBlocksModel(admin.ModelAdmin):
    list_filter = ('id_lb',)
    list_display = ('id_lb',)


@admin.register(Lessons)
class LessonsModel(admin.ModelAdmin):
    list_filter = ('id_les', 'name_les', 'id_lb')
    list_display = ('id_les', 'name_les', 'id_lb')


@admin.register(Lexemes)
class LexemesModel(admin.ModelAdmin):
    list_filter = ('id_lex', 'mean_lex', 'transcr', 'stress', 'type_lex', 'id_les')
    list_display = ('id_lex', 'mean_lex', 'transcr', 'stress', 'type_lex', 'id_les')


@admin.register(Media)
class MediaModel(admin.ModelAdmin):
    list_filter = ('id_med', 'link_med', 'id_lex', 'med_type')
    list_display = ('id_med', 'link_med', 'id_lex', 'med_type')


@admin.register(Ik)
class IkModel(admin.ModelAdmin):
    list_filter = ('id_ik',)
    list_display = ('id_ik',)


@admin.register(Replicas)
class ReplicasModel(admin.ModelAdmin):
    list_filter = ('id_rep', 'time_start', 'time_finish', 'id_lex', 'id_med', 'id_ik', 'med_ik')
    list_display = ('id_rep', 'time_start', 'time_finish', 'id_lex', 'id_med', 'id_ik', 'med_ik')


@admin.register(LecFilling)
class LecFillingModel(admin.ModelAdmin):
    list_filter = ('id', 'id_lex', 'id_lex_cons')
    list_display = ('id', 'id_lex', 'id_lex_cons')


admin.site.register(Rules)


class RulesModel(admin.ModelAdmin):
    list_filter = ('id_r', 'picture', 'id_les', 'id_lex')
    list_display = ('id_r', 'picture', 'id_les', 'id_lex')


admin.site.register(RulesLexemes)


# class RulesLexemesModel(admin.ModelAdmin):
#     list_filter = ('id_r','id_lex')
#     list_display = ('id_r','id_lex')

@admin.register(TypesEx)
class TypesExModel(admin.ModelAdmin):
    list_filter = ('type_ex', 'mean_type_ex')
    list_display = ('type_ex', 'mean_type_ex')


@admin.register(Exercises)
class ExercisesModel(admin.ModelAdmin):
    list_filter = ('id_ex', 'type_ex', 'id_les', 'num_ex')
    list_display = ('id_ex', 'type_ex', 'id_les', 'num_ex')


@admin.register(Progress)
class ProgressModel(admin.ModelAdmin):
    list_filter = ('id_ex', 'login', 'mean_pr')
    list_display = ('id_ex', 'login', 'mean_pr')


@admin.register(Tasks)
class TasksModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'id_lex_right', 'type_med', 'num_lex', 'count_miss')
    list_display = ('id_task', 'id_ex', 'num_task', 'id_lex_right', 'type_med', 'num_lex', 'count_miss')


@admin.register(Variants)
class VariantsModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_lex', 'num_miss')
    list_display = ('id_task', 'id_lex', 'num_miss')


@admin.register(Favorites)
class FavoritesModel(admin.ModelAdmin):
    list_filter = ('id_ex', 'id_lex', 'id_med', 'login')
    list_display = ('id_ex', 'id_lex', 'id_med', 'login')


@admin.register(Newletters)
class NewlettersModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'med_type', 'link_med')
    list_display = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'med_type', 'link_med')


@admin.register(Newwords)
class NewwordsModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'med_type', 'link_med')
    list_display = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'med_type', 'link_med')


@admin.register(Newphrases)
class NewphrasesModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'med_type', 'link_med')
    list_display = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'med_type', 'link_med')


@admin.register(Matchsyllablessound)
class MatchsyllablessoundModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'right_sound', 'wrong_sound')
    list_display = ('id_task', 'id_ex', 'num_task', 'mean_lex', 'right_sound', 'wrong_sound')


@admin.register(Collectwordsletters)
class CollectwordslettersModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'word')
    list_display = ('id_task', 'id_ex', 'num_task', 'word')


@admin.register(Missingletter)
class MissingletterModel(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'word', 'num_lex', 'count_miss', 'num_miss', 'letter')
    list_display = ('id_task', 'id_ex', 'num_task', 'word', 'num_lex', 'count_miss', 'num_miss', 'letter')


@admin.register(Pronunciationwords)
class Pronunciationwords(admin.ModelAdmin):
    list_filter = ('id_ex', 'mean_lex', 'id_task', 'num_task', 'right_sound', 'wrong_sound')
    list_display = ('id_ex', 'mean_lex', 'id_task', 'num_task', 'right_sound', 'wrong_sound')


@admin.register(Recoverphrases)
class Pronunciationwords(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'word')
    list_display = ('id_task', 'id_ex', 'num_task', 'word')


@admin.register(Selectwords)
class Selectwords(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'phrase', 'num_lex', 'count_miss', 'num_miss', 'word')
    list_display = ('id_task', 'id_ex', 'num_task', 'phrase', 'num_lex', 'count_miss', 'num_miss', 'word')


@admin.register(Wordpicturematch)
class Wordpicturematch(admin.ModelAdmin):
    list_filter = ('id_ex', 'id_task', 'num_task', 'var1_lex', 'var1_pic', 'var_lex', 'var_pic')
    list_display = ('id_ex', 'id_task', 'num_task', 'var1_lex', 'var1_pic', 'var_lex', 'var_pic')


@admin.register(Wordpictureselect)
class Pronunciationwords(admin.ModelAdmin):
    list_filter = ('id_ex', 'id_task', 'num_task', 'right_lex', 'right_pic', 'wrong_lex', 'wrong_pic')
    list_display = ('id_ex', 'id_task', 'num_task', 'right_lex', 'right_pic', 'wrong_lex', 'wrong_pic')


@admin.register(Writewords)
class Writewords(admin.ModelAdmin):
    list_filter = ('id_task', 'id_ex', 'num_task', 'phrase', 'num_lex', 'count_miss', 'word')
    list_display = ('id_task', 'id_ex', 'num_task', 'phrase', 'num_lex', 'count_miss', 'word')
