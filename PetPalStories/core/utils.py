from PetPalStories.stories.models import Story

MAX_LAST_SEEN = 6


def get_last_seen_unique(pk_list, model):
    display_last_6 = []
    for pk in pk_list:
        model_obj = model.objects.filter(pk=pk) or None
        if len(display_last_6) >= MAX_LAST_SEEN:
            return display_last_6
        if model_obj is not None and model_obj.get() not in display_last_6:
            display_last_6.append(model_obj.get())
    return display_last_6