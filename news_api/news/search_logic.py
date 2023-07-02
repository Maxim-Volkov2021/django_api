from django.db.models import Q

def character_definition_for_query(text, param):
    # list_math_method = [":", "~"]
    list_name_news = ["id", "title", "content", "author__id", 'author__name', "tags__id", "tags__name"]
    list_name_tags = ["id", "name"]
    list_name_authors = ["id", "name"]
    list_name = []
    if param == "news":
        list_name = list_name_news
    elif param == "tags":
        list_name = list_name_tags
    elif param == "authors":
        list_name = list_name_authors

    result = None
    if ":" in text:
        name_and_value = text.split(":")
        name_and_value[0] = name_and_value[0].replace(".", "__").strip()
        if len(name_and_value) == 2 and name_and_value[0] in list_name:
            temp = {name_and_value[0]: name_and_value[1]}
            result = Q(**temp)
    if "~" in text:
        name_and_value = text.split("~")
        name_and_value[0] = name_and_value[0].replace(".", "__").strip()
        if len(name_and_value) == 2 and name_and_value[0] in list_name:
            temp = {name_and_value[0] + "__contains": name_and_value[1]}
            result = Q(**temp)
    return result


def search_with_AND_OR(request, param):
    text_query = request.GET["query"]
    symbol_AND = " AND "
    symbol_OR = " OR "
    AND_query = None
    OR_query = None
    query = None

    if symbol_AND in text_query:
        AND_list = text_query.split(symbol_AND)
        AND_query_list = []
        for i in range(len(AND_list)):
            if symbol_OR in AND_list[i]:
                OR_list = AND_list[i].split(symbol_OR)
                OR_query_list = []

                for j in range(len(OR_list)):
                    OR_query_list.append(character_definition_for_query(OR_list[j], param))
                    if OR_query_list[len(OR_query_list) - 1] != None and OR_query == None:
                        OR_query = OR_query_list[len(OR_query_list) - 1]
                    elif OR_query_list[len(OR_query_list) - 1] != None:
                        OR_query.add(OR_query_list[len(OR_query_list) - 1], Q.OR)

                if AND_query == None and OR_query != None:
                    AND_query = OR_query
                elif AND_query != None and OR_query != None:
                    AND_query.add(OR_query, Q.AND)

                OR_query = None


            else:
                AND_query_list.append(character_definition_for_query(AND_list[i], param))
                if AND_query_list[len(AND_query_list) - 1] != None and AND_query == None:
                    AND_query = AND_query_list[len(AND_query_list) - 1]
                elif AND_query_list[len(AND_query_list) - 1] != None:
                    AND_query.add(AND_query_list[len(AND_query_list) - 1], Q.AND)

            if (len(AND_list) - 1) == i:
                query = AND_query

    elif symbol_OR in text_query:
        OR_list = text_query.split(symbol_OR)
        OR_query_list = []
        for j in range(len(OR_list)):
            OR_query_list.append(character_definition_for_query(OR_list[j], param))
            if OR_query_list[len(OR_query_list) - 1] != None and OR_query == None:
                OR_query = OR_query_list[len(OR_query_list) - 1]
            elif OR_query_list[len(OR_query_list) - 1] != None:
                OR_query.add(OR_query_list[len(OR_query_list) - 1], Q.OR)
        query = OR_query
    else:
        query = character_definition_for_query(text_query, param)

    return query


