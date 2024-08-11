import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://db_224142778_sit722_part1_gssv_user:odZ588gSVTCh9oaV2OqW2w5OEitfGvla@dpg-cqs674ggph6c73a7ikgg-a.singapore-postgres.render.com/db_224142778_sit722_part1_gssv")

settings = Settings()
