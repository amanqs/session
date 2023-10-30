from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import env


mongo = MongoCli(config.MONGO_URL)
db = mongo.AmangString
