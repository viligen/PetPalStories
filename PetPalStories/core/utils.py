from PetPalStories.stories.models import Story

MAX_LAST_SEEN = 6


def get_last_seen_unique(pk_list):
    display_last_6 = []
    for pk in pk_list:
        story_obj = Story.objects.filter(pk=pk) or None
        if len(display_last_6) >= MAX_LAST_SEEN:
            return display_last_6
        if story_obj is not None and story_obj.get() not in display_last_6:
            display_last_6.append(story_obj.get())
    return display_last_6