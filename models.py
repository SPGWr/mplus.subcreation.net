from google.appengine.ext import ndb

# store all the runs
class Run(ndb.Model):
    roster = ndb.StringProperty(repeated=True)
    score = ndb.FloatProperty(indexed=False)

# top 20 runs for a specific dungeon affix combo in a region
class DungeonAffixRegion(ndb.Model):
    # when were these data last updated
    last_updated = ndb.DateTimeProperty(auto_now_add=True)
   
    # which dungeon
    dungeon = ndb.StringProperty()
    # which affixes
    affixes = ndb.StringProperty()
    # which region
    region = ndb.StringProperty()

    runs = ndb.LocalStructuredProperty(Run, repeated=True)

class KnownAffixes(ndb.Model):
    affixes = ndb.StringProperty()
    first_seen = ndb.DateTimeProperty(auto_now_add=True)

