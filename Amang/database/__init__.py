from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import env


mongo = MongoCli(env.MONGO_URL)
db = mongo.AmangString
