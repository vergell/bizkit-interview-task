from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):

    if not args:
        return USERS
    else:
        results = []
        for key in args:
            for user in USERS:
                if key=='age':
                    age_int = int(args[key])
                    ages = [str(age_int-1), str(age_int), str(age_int+1)]
                    ages_str = " ".join(ages)
                    if str(user[key]) in ages_str and user not in results:
                            results.append(user)
                else:
                    if str(args[key]).lower() in str(user[key]).lower() and user not in results:
                        results.append(user)

    return results
