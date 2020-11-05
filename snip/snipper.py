from . import db
from .models import Snip

import logging
import secrets
import base58

log = logging.getLogger(__name__)


def snip(url: str, reusable=False) -> str:
    if reusable:
        log.debug("Snipping is marked reusable. Looking for existing reusable snips.")
        reusable_snip = Snip.query.filter(Snip.url == url,
                                          Snip.reusable == True).first()
        if reusable_snip:
            log.debug(f"Found reusable snip {reusable_snip} for URL {url}")
            return reusable_snip.snip
        else:
            log.debug(f"No reusable snips exist. Generating new snip.")

    snip = gen_snip()
    log.debug(f"Generated snip: {snip}")

    while Snip.query.filter(Snip.snip == snip).first():
        log.info(f"Snip {snip} for {url} already exists. Generating new snip.")
        snip = gen_snip()
        log.debug(f"Generated new snip: {snip}")

    log.info(f"Using snip {snip} for URL {url}")
    db.session.add(Snip(url=url, snip=snip, reusable=reusable))
    db.session.commit()
    return snip


def gen_snip():
    """ Generate a random snip """
    rand = secrets.token_bytes(5)
    snip = str(base58.b58encode(rand), 'ascii')
    return snip


def unsnip(snip: str):
    snip_dao = Snip.query.filter(Snip.snip == snip).first()
    if snip_dao:
        return snip_dao.url
    return None
