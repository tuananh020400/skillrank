from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Challenge, TestCase
from apps.core.models import Company


def create_challenge(request):
    if request.method == 'POST':
        # Get company from session
        company_id = request.session.get('company_id')
        if not company_id:
            messages.error(request, 'You must be logged in as a company to create a challenge.')
            return redirect('create_challenge')

        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            messages.error(request, 'Company not found.')
            return redirect('create_challenge')

        # Get form data
        title = request.POST.get('title', '').strip()
        category = request.POST.get('category', '')
        difficulty = request.POST.get('difficulty', 'EASY').upper()
        reward_points = request.POST.get('reward_points', 100)
        description = request.POST.get('description', '')
        requirements = request.POST.get('requirements', '')
        required_skills = request.POST.get('required_skills', '')
        status = request.POST.get('status', 'ACTIVE')

        # Validation
        if not title:
            messages.error(request, 'Challenge title is required.')
            return redirect('create_challenge')

        try:
            reward_points = int(reward_points)
        except (ValueError, TypeError):
            reward_points = 100
        
        # Create Challenge
        challenge = Challenge.objects.create(
            title=title,
            company=company,
            category=category,
            difficulty=difficulty,
            reward_points=reward_points,
            description=description,
            requirements=requirements,
            required_skills=required_skills,
            status=status.upper(),
        )
        print(challenge)

        # Create Test Cases
        test_inputs = request.POST.getlist('test_input[]')
        test_outputs = request.POST.getlist('test_output[]')
        test_hiddens = request.POST.getlist('test_hidden[]')

        for inp, out, hid in zip(test_inputs, test_outputs, test_hiddens):
            if inp.strip() or out.strip():
                TestCase.objects.create(
                    challenge=challenge,
                    input_data=inp.strip(),
                    expected_output=out.strip(),
                    is_hidden=(hid == '1'),
                )

        if challenge.status == 'DRAFT':
            messages.success(request, f'Challenge "{challenge.title}" saved as draft!')
        else:
            messages.success(request, f'Challenge "{challenge.title}" published successfully!')

        return redirect('create_challenge')

    return render(request, 'challenges/create_challenge.html')