from django.db import models


class Course(models.Model):
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    crn = models.CharField(
        primary_key=True,
        max_length=32,
        db_index=True,
        verbose_name="CRN",
    )
    subject = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Subject",
    )
    course_id = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Course ID",
    )
    course_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Course Name",
    )
    units = models.IntegerField(
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Units",
    )
    type = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Type",
    )
    days = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        db_index=True,
    )
    hours = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        db_index=True,
    )
    room = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        db_index=True,
    )
    dates = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    instructor = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Instructor",
    )
    # TODO needs work
    lecture_crn = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Lecture CRN",
    )
    term = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Term",
    )
    capacity = models.IntegerField(
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Capacity",
    )
    enrolled = models.IntegerField(
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Enrolled",
    )
    available = models.IntegerField(
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Available",
    )
    final_type = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_days = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_hours = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_room = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_dates = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_type_2 = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_days_2 = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_hours_2 = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_room_2 = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    final_dates_2 = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )

    def __str__(self):
        return self.crn