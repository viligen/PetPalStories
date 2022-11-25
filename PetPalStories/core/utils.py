from PetPalStories.stories.models import Story

MAX_LAST_SEEN = 5


def get_last_seen_unique(pk_list):
    display_last_5 = []
    for pk in pk_list:
        story_obj = Story.objects.filter(pk=pk) or None
        if len(display_last_5) >= MAX_LAST_SEEN:
            return display_last_5
        if story_obj is not None and story_obj.get() not in display_last_5:
            display_last_5.append(story_obj.get())
    return display_last_5