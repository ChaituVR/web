from haystack import indexes

from .models import UserDirectory


class UserDirectoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    profile_id = indexes.IntegerField(null=True,model_attr='profile_id')
    join_date = indexes.CharField(null=True,model_attr='join_date')
    github_created_at = indexes.CharField(null=True,model_attr='github_created_at')
    email = indexes.CharField(null=True,model_attr='email_if_not_supressed')
    first_name = indexes.CharField(null=True,model_attr='first_name', faceted=True)
    last_name = indexes.CharField(null=True,model_attr='last_name', faceted=True)
    handle = indexes.CharField(null=True,model_attr='handle', faceted=True)
    sms_verification = indexes.BooleanField(null=True,model_attr='sms_verification',faceted=True)
    persona = indexes.CharField(null=True,model_attr='persona',faceted=True)
    rank_coder = indexes.IntegerField(null=True,model_attr='rank_coder',faceted=True)
    rank_funder = indexes.IntegerField(null=True,model_attr='rank_funder',faceted=True)
    num_hacks_joined = indexes.IntegerField(null=True,model_attr='num_hacks_joined',faceted=True)
    which_hacks_joined = indexes.MultiValueField(null=True,model_attr='which_hacks_joined',faceted=True)
    hack_work_starts = indexes.IntegerField(null=True,model_attr='hack_work_starts',faceted=True)
    hack_work_submits = indexes.IntegerField(null=True,model_attr='hack_work_submits',faceted=True)
    hack_work_start_orgs = indexes.MultiValueField(null=True,model_attr='hack_work_start_orgs',faceted=True)
    hack_work_submit_orgs = indexes.MultiValueField(null=True,model_attr='hack_work_submit_orgs',faceted=True)
    bounty_work_starts = indexes.IntegerField(null=True,model_attr='bounty_work_starts',faceted=True)
    bounty_work_submits = indexes.IntegerField(null=True,model_attr='bounty_work_submits',faceted=True)
    hack_started_feature = indexes.IntegerField(null=True,model_attr='hack_started_feature',faceted=True)
    hack_started_code_review = indexes.IntegerField(null=True,model_attr='hack_started_code_review',faceted=True)
    hack_started_security = indexes.IntegerField(null=True,model_attr='hack_started_security',faceted=True)
    hack_started_design = indexes.IntegerField(null=True,model_attr='hack_started_design',faceted=True)
    hack_started_documentation = indexes.IntegerField(null=True,model_attr='hack_started_documentation',faceted=True)
    hack_started_bug = indexes.IntegerField(null=True,model_attr='hack_started_bug',faceted=True)
    hack_started_other = indexes.IntegerField(null=True,model_attr='hack_started_other',faceted=True)
    hack_started_improvement = indexes.IntegerField(null=True,model_attr='hack_started_improvement',faceted=True)
    started_feature = indexes.IntegerField(null=True,model_attr='started_feature',faceted=True)
    started_code_review = indexes.IntegerField(null=True,model_attr='started_code_review',faceted=True)
    started_security = indexes.IntegerField(null=True,model_attr='started_security',faceted=True)
    started_design = indexes.IntegerField(null=True,model_attr='started_design',faceted=True)
    started_documentation = indexes.IntegerField(null=True,model_attr='started_documentation',faceted=True)
    started_bug = indexes.IntegerField(null=True,model_attr='started_bug',faceted=True)
    started_other = indexes.IntegerField(null=True,model_attr='started_other',faceted=True)
    started_improvement = indexes.IntegerField(null=True,model_attr='started_improvement',faceted=True)
    submitted_feature = indexes.IntegerField(null=True,model_attr='submitted_feature',faceted=True)
    submitted_code_review = indexes.IntegerField(null=True,model_attr='submitted_code_review',faceted=True)
    submitted_security = indexes.IntegerField(null=True,model_attr='submitted_security',faceted=True)
    submitted_design = indexes.IntegerField(null=True,model_attr='submitted_design',faceted=True)
    submitted_documentation = indexes.IntegerField(null=True,model_attr='submitted_documentation',faceted=True)
    submitted_bug = indexes.IntegerField(null=True,model_attr='submitted_bug',faceted=True)
    submitted_other = indexes.IntegerField(null=True,model_attr='submitted_other',faceted=True)
    submitted_improvement = indexes.IntegerField(null=True,model_attr='submitted_improvement',faceted=True)
    bounty_earnings = indexes.FloatField(null=True,model_attr='bounty_earnings',faceted=True)
    bounty_work_start_orgs = indexes.MultiValueField(null=True,model_attr='bounty_work_start_orgs',faceted=True)
    bounty_work_submit_orgs = indexes.MultiValueField(null=True,model_attr='bounty_work_submit_orgs',faceted=True)
    kudos_sends = indexes.IntegerField(null=True,model_attr='kudos_sends',faceted=True)
    kudos_receives = indexes.IntegerField(null=True,model_attr='kudos_receives',faceted=True)
    hack_winner_kudos_received = indexes.IntegerField(null=True,model_attr='hack_winner_kudos_received',faceted=True)
    grants_opened = indexes.IntegerField(null=True,model_attr='grants_opened',faceted=True)
    grant_contributed = indexes.IntegerField(null=True,model_attr='grant_contributed',faceted=True)
    grant_contributions = indexes.IntegerField(null=True,model_attr='grant_contributions',faceted=True)
    grant_contribution_amount = indexes.FloatField(null=True,model_attr='grant_contribution_amount',faceted=True)
    num_actions = indexes.IntegerField(null=True,model_attr='num_actions',faceted=True)
    action_points = indexes.IntegerField(null=True,model_attr='action_points',faceted=True)
    avg_points_per_action = indexes.FloatField(null=True,model_attr='avg_points_per_action',faceted=True)
    last_action_on = indexes.CharField(null=True,model_attr='last_action_on')
    keywords = indexes.MultiValueField(null=True,model_attr='keywords', faceted=True)
    activity_level = indexes.CharField(null=True,model_attr='activity_level',faceted=True)
    reliability = indexes.CharField(null=True,model_attr='reliability',faceted=True)
    average_rating = indexes.FloatField(null=True,model_attr='average_rating',faceted=True)
    longest_streak = indexes.IntegerField(null=True,model_attr='longest_streak',faceted=True)
    earnings_count = indexes.FloatField(null=True,model_attr='earnings_count',faceted=True)
    follower_count = indexes.IntegerField(null=True,model_attr='follower_count',faceted=True)
    following_count = indexes.IntegerField(null=True,model_attr='following_count',faceted=True)
    num_repeated_relationships = indexes.IntegerField(null=True,model_attr='num_repeated_relationships',faceted=True)
    verification_status = indexes.CharField(null=True,model_attr='verification_status',faceted=True)

    def get_model(self):
        return UserDirectory

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
