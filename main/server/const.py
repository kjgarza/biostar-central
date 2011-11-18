"""
Various constants used throught the site
"""

# The name of the editor group
MODERATOR_GROUP = 'mod_group'

# Permissions granted to everybody
EVERYONE_PERM = ['add_comment','add_post','edit_post']

# Permissions that can be gained with enough reputation.
# Mods and admins automatically have all of these
REPUTATION_PERM = {
    'vote_up':15,
    'vote_down':100,
}

# Permissions granted only to admins and moderators. Admins have mod permissions.
MODERATOR_PERM = ['moderate_post', 'view_deleted']
ADMIN_PERM = []

# I added here anything that I could think of for the future rather than
# all post types that are to be implemented. This could make life a lot easier in the future
POST_VALS =  "Post Question Answer Comment Guide Blog News Opinion Announcement Article Other".split()
POST_NUMS = range(len(POST_VALS))
POST_CHOICES = zip( POST_NUMS, POST_VALS )
POST_MAP = dict(zip( POST_VALS, POST_NUMS ))
POST_QUESTION = POST_MAP['Question']
POST_ANSWER   = POST_MAP['Answer']

# User types
USER_NORMAL, USER_MODERATOR, USER_ADMIN = 0, 1, 2
USER_TYPES = ((USER_NORMAL, 'Member'), (USER_MODERATOR, 'Moderator'), (USER_ADMIN, 'Administrator'))

# Revision constants
REV_NONE, REV_CLOSE, REV_REOPEN, REV_DELETE, REV_UNDELETE = 0, 1, 2, 3, 4
REV_ACTIONS = (
    (REV_NONE, ''), (REV_CLOSE, 'Close'), (REV_REOPEN, 'Reopen'),
    (REV_DELETE, 'Delete'), (REV_UNDELETE, 'Undelete')
)
REV_ACTION_MAP = dict(REV_ACTIONS)

VOTE_UP, VOTE_DOWN, VOTE_ACCEPT = 0, 1, 2

VOTE_TYPES = ((VOTE_UP, 'Upvote'), (VOTE_DOWN, 'Downvote'), (VOTE_ACCEPT, 'Accept'))

OPPOSING_VOTES = { VOTE_UP:VOTE_DOWN, VOTE_DOWN:VOTE_UP } # Mappings of mutually exclusive votes

# post score changes
POST_SCORE = { VOTE_UP:1, VOTE_DOWN:-1 }

# user reputation changes
USER_REP  = { VOTE_UP:10, VOTE_DOWN:-2, VOTE_ACCEPT:15 }
VOTER_REP = { VOTE_DOWN: -1, VOTE_ACCEPT:2 }
