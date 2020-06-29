import enum
from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    c_s = "CS"
    java_script = "JAVASCRIPT"
    java = "JAVA"
    php = "PHP"
    ruby = "RUBY"

class DescriptionType(BaseEnumClass, enum.Enum):
    text = "TEXT"
    html = "HTML"
    mark_down = "MARKDOWN"


CodeLanguageList = [code_language.value for code_language in CodeLanguage]


DescriptionTypeList = [
    description_type.value for description_type in DescriptionType
]