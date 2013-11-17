from django.conf import settings
import stripe


def charge_payment(amount_in_dollars, token, description):
  stripe.api_key = settings.STRIPE_SECRET_KEY
  token_id = token['id']
  amount_in_cents = int(amount_in_dollars * 100)

  charge = stripe.Charge.create(
    amount=amount_in_cents,
    currency="usd",
    card=token_id,
    description=description
  )

  return charge
