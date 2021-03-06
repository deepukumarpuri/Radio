from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["country", "countryinfo"]), group=1)
async def country_info(bot, update: Message):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""--**Country Information**--
đ <b>Name</b> : `{country.name()}`
đ¤ <b>Native Name</b> : `{country.native_name()}`
đ°ī¸ <b>Capital</b> : `{country.capital()}`
đĨ <b>Population</b> : `{country.population()}`
đ <b>Region</b> : `{country.region()}`
đī¸ <b>Sub Region</b> : `{country.subregion()}`
âĄī¸ <b>Top Level Domains</b> : `{country.tld()}`
đ <b>Calling Codes</b> : `{country.calling_codes()}`
đĩ <b>Currencies</b> : `{country.currencies()}`
đˇī¸ <b>Residence</b> : `{country.demonym()}`
â˛ī¸ <b>Timezone</b> : `{country.timezones()}`
<b>ÂŠī¸ Made by</b> **@DKBOTZ**"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google', url=f'https://www.google.com/search?q={country_name}')
        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
