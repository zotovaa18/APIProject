from drf_yasg.generators import OpenAPISchemaGenerator


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
  def get_schema(self, request=None, public=False):
    """Generate a :class:`.Swagger` object with custom tags"""

    swagger = super().get_schema(request, public)
    swagger.tags = [
        {
            "name": "countries",
            "description": "Набор методов для работы с данными о странах"
        },
        {
            "name": "exercises",
            "description": "Набор методов для работы с данными об упражнениях урока"
        },
        {
            "name": "favorites",
            "description": "Набор методов для работы с избранными данными пользователей"
        },
        {
            "name": "ik",
            "description": "Набор методов для работы с данными об интонационных конструкциях"
        },
        {
            "name": "lecfilling",
            "description": "Набор методов для работы с данными об наполнении лексем"
        },
        {
            "name": "lessonblocks",
            "description": "Набор методов для работы с данными об блоках уроков"
        },
        {
            "name": "lessons",
            "description": "Набор методов для работы с данными об уроках"
        },
        {
            "name": "lexemes",
            "description": "Набор методов для работы с данными об лексемах"
        },
        {
            "name": "people",
            "description": "Набор методов для работы с данными о пользователей"
        },
        {
            "name": "peoplegroups",
            "description": "Набор методов для работы с данными о группах пользователей"
        },
        {
            "name": "progress",
            "description": "Набор методов для работы с данными о прогрессе пользователя"
        },
        {
            "name": "replicas",
            "description": "Набор методов для работы с данными о репликах"
        },
        {
            "name": "rules",
            "description": "Набор методов для работы с данными о правилах"
        },
        {
            "name": "ruleslexemes",
            "description": "Набор методов для работы с данными о лексем в правилах"
        },
        {
            "name": "showinfoaboutphrase",
            "description": "дто для экранов с фразами"
        },
        {
            "name": "showinfoaboutrules",
            "description": "дто для экранов с правилами"
        },
        {
            "name": "showinfoaboutwordsletters",
            "description": "дто для экранов с буквами-словами "
        },
        {
            "name": "status",
            "description": "Набор методов для работы с данными о статусах"
        },
        {
            "name": "tasks",
            "description": "Набор методов для работы с данными о заданиях в упражнении"
        },
        {
            "name": "typesex",
            "description": "Набор методов для работы с данными о типах упражнений"
        },
        {
            "name": "typesmed",
            "description": "Набор методов для работы с данными о типах медиа"
        },
        {
            "name": "variants",
            "description": "Набор методов для работы с данными вариантов для упражнений"
        },
        {
            "name": "vowelsound",
            "description": "Набор методов для работы с данными о звуках гласных"
        },
        {
            "name": "typeslex",
            "description": "Набор методов для работы с данными типов упражнений"
        },



    ]

    return swagger