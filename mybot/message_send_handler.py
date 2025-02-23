# from aiogram import types
# from mybot.loader import dp, mybot
#
#
# # Replace with actual group IDs
# SOURCE_GROUP_ID = -1001111111111
# TARGET_GROUP_ID = -1002457389396
#
# @dp.message_handler(content_types=types.ContentTypes.TEXT, chat_id=SOURCE_GROUP_ID)
# async def forward_non_admin_messages(message: types.Message):
#     """
#     Picks non-admin user messages from the source group, deletes them,
#     and forwards them to the target group.
#     """
#     # Get admin user IDs of the source group
#     chat_administrators = await mybot.get_chat_administrators(SOURCE_GROUP_ID)
#     admin_ids = [admin.user.id for admin in chat_administrators]
#
#     if message.from_user.id not in admin_ids:
#         try:
#             # Forward message to the target group
#             await mybot.send_message(
#                 chat_id=TARGET_GROUP_ID,
#                 text=(
#                     f"📩 New Message from @{message.from_user.username or message.from_user.full_name}:\n"
#                     f"{message.text}"
#                 )
#             )
#             # Delete original message from source group
#             await message.delete()
#
#         except Exception as e:
#             print(f"Error: {e}")
