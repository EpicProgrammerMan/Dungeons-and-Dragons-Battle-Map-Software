def init_db():
    """ import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db() """
    from battlemap.models.database import engine, Base
    from battlemap.models.players import PlayerModel
    from battlemap.models.enemies import EnemyModel
    Base.metadata.create_all(bind=engine)