from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["country", "countryinfo"]), group=1)
async def country_info(bot, update: Message):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""--**Country Information**--
🌐 <b>Name</b> : `{country.name()}`
🔤 <b>Native Name</b> : `{country.native_name()}`
🕰️ <b>Capital</b> : `{country.capital()}`
👥 <b>Population</b> : `{country.population()}`
🌏 <b>Region</b> : `{country.region()}`
🏖️ <b>Sub Region</b> : `{country.subregion()}`
➡️ <b>Top Level Domains</b> : `{country.tld()}`
📞 <b>Calling Codes</b> : `{country.calling_codes()}`
💵 <b>Currencies</b> : `{country.currencies()}`
🏷️ <b>Residence</b> : `{country.demonym()}`
⏲️ <b>Timezone</b> : `{country.timezones()}`
<b>©️ Made by</b> **@DKBOTZ**"""
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
