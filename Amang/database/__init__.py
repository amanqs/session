from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import config


mongo = MongoCli(config.MONGO_URL)
db = mongo.AmangString
