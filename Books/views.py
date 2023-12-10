from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Books, Feedback
from .forms import FeedbackForm

def index(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        newest_Books = Books.objects.order_by('-publication_date')[:15]
        context = {'newest_Books': newest_Books}
        return render(request, 'Books/index.html', context)
    else:
        # You can customize this part to display a message or redirect to the sign-in page
        return render(request, 'Books/index_unauthenticated.html')

def show(request, Books_id):
    # Use get_object_or_404 to retrieve the book or raise a 404 error if not found
    book = get_object_or_404(Books, pk=Books_id)
    
    # Pass the book object to the template
    return render(request, 'Books/show.html', {'book': book})

def save_feedback(request, book_id):
    book = get_object_or_404(Books, pk=book_id)

    # Fetch all feedbacks for the current book
    all_feedback = Feedback.objects.filter(book=book)

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_text = form.cleaned_data['feedback_text']

            # Save feedback to the database
            feedback = Feedback.objects.create(book=book, feedback_text=feedback_text)

            # Update the feedbacks list
            all_feedback = Feedback.objects.filter(book=book)

            # Pass the feedback to the template
            return render(request, 'Books/save_feedback.html', {'form': form, 'book': book, 'all_feedback': all_feedback})
    else:
        form = FeedbackForm()

    # Pass the feedback to the template
    return render(request, 'Books/save_feedback.html', {'form': form, 'book': book, 'all_feedback': all_feedback})

def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    book_id = feedback.book.id

    # Delete the feedback
    feedback.delete()

    # Redirect back to the feedback page
    return redirect('Books:save_feedback', book_id=book_id)

def update_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    book_id = feedback.book.id

    if request.method == "POST":
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('Books:save_feedback', book_id=book_id)
    else:
        form = FeedbackForm(instance=feedback)

    return render(request, 'Books/update_feedback.html', {'form': form, 'book': feedback.book})