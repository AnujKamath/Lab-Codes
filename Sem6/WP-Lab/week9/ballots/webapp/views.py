from django.shortcuts import render, redirect
from .forms import VoteForm
from .models import Vote

def vote_view(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            user_choice = form.cleaned_data['choice']
            vote, created = Vote.objects.get_or_create(choice=user_choice)
            vote.count += 1
            vote.save()
            return redirect('vote')
    else:
        form = VoteForm()

    votes = Vote.objects.all()
    total_votes = sum(vote.count for vote in votes)

    if total_votes == 0:
        percentages = {'Good': 0, 'Satisfactory': 0, 'Bad': 0}
    else:
        percentages = {
            vote.choice: round((vote.count / total_votes) * 100)
            for vote in votes
        }

    return render(request, 'base.html', {
        'form': form,
        'percentages': percentages,
    })
